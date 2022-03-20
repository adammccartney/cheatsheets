# An installable django app (where to draw the line)

```
Stand, stand at the window
  As the tears scald and start;
You shall love your crooked neighbor
  With your crooked heart.
                         - W.H. Auden, Another Time
```

Faced with the task of coordinating the package managment for a very messy
django project, there is a case where I need to copy changes being pushed into
a demo project to what is basically a very similar project that is used for
testing our individual apps before releasing tagged versions.

## Existing methods

There is a really good article on how to write [installable django apps](https://realpython.com/installable-django-app/)
over on real python. Much of the info here was of a great help. Unfortunately,
the django application that we're dealing with is a fairly complex webapp, with
a bunch of subcomponents, many of whom have interdependencies. As outlined in
the article, one of the issues with creating installable django apps is that
they need to be standalone python packages. This means that each one of our
subcomponents needs to be extracted from the parent project in order to be
packaged and released. The article outlines an approach for using scripts to
bootstrap the individual apps in order to test them outside the context of a
django project (i.e. within the context of a python package).

## Specifics of our case

Our case is a little different - we want to extract appA and appB, making them both installable
packages. The reason for doing this is that we want to use their functionality
in a bunch of other django applications. However, we don't want to spend the
next 3 weeks trying to figure out a clean way out of all the interdependencies
between the apps. For our specific use case, the first approach that we are
going to try is to leverage Git and Gitlab to create a release pipeline for the
packages. The upstream package is still going to be the `django-base` app,
where we will test out all our components, add new features etc. We then want
to create a tagged release that we can track from the repositories where our
subcomponents live.

```
example of django app with subcomponents

django-base/
├── appA
├── appB
├── config
│   ├── __init__.py
│   ├── locale
│   ├── settings
│   ├── static
│   ├── urls.py
│   └── wsgi.py
├── home
│   ├── blocks.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── static
│   └── templates
├── locale
│   ├── de
│   └── en
├── log
│   └── portal
├── manage.py
└── search
    ├── __init__.py
    ├── templates
    └── views.py

```

Generally speaking a django app is developed in the context of a django
project. That is we don't really develop it as an upstream package and then
install it when we have the features that we want. Instead, we add the features
incrementally using an `example_project`. As the article above suggests, it's
no harm to include the sample project in the directory of the django app that
you wish to make installable. It's worth pointing out that in this case, the

```
example of subcomponent package

.
├── example_project
│   ├── appA
│   ├── appB
│   ├── config
│   ├── home
│   ├── locale
│   ├── log
│   ├── manage.py
│   └── search
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
└── setup.py

```

When it has all the features that you want, you can simply move the component out
of the `example_project` into the parent directory for packaging.

```
.
├── appA
├── example-project
│   ├── appB
│   ├── config
│   ├── home
│   ├── locale
│   ├── log
│   ├── manage.py
│   └── search
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
└── setup.py
```

## Keeping things up-to-date (thank god for unix)

One of the challenges with the wrangling that is going on here is that there is
a developer making changes to another cloned version of `django-base` called
`django-prod` that being used in production. He is a graduate of the [it works on my machine program](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/)
and this is just his way of working. While this sounds like a bit of a
headache, it's actually not that bad (considering that I'm far from perfect
myself). The workflow that we have going at the moment is that I am doing a
daily `patch` of his changes. Obviously I'm not the first software developer to
have to do such a thing, and actually there exist really nice unix tools for
the job. Enter `diff` and `patch`. `diff` is well known and allows you to see
what differences exist between two files (or directories). `patch` was less
well known to me, I think I first read about in in [The Art of Unix
Programming](https://archive.org/details/ost-computer-science-the_art_of_unix_programming-1)
(which apparently is free, like all the best things in life).
Anyway, `patch` lets you ... well, patch a file with new changes. Presumably
this is also how git merge is working.

### Patching files

1. Create a patchfile by diffing the two files and piping the output to a
   patchfile

```
diff -u file1 file2 > patchfile.patch
```

2. Apply the patch

```
patch file1 patchfile.patch
```

### Patching directories

1. Create a patchfile by running diff on the two directories and piping the
   output to a patchfile

```
diff -ruN folder1/ folder2/ > patchfile.patch
```

2. Apply the patch

```
patch -s -p0 < patchfile.patch
```

## Creating an automated deployment pipeline for releases

As mentioned at the outset, we want to leverage CI pipelines to automate some
of these steps. It's not uncommon or unheard of for web applications to be
written and deployed under very tight time constraints. The people that end up
writing them can often be stretched really thin and not have the resources at
their disposal to come up with super clean lines in terms of how the project is
designed and implemented. It's nice to imagine that we all would architect
projects like a modern day Palladio.

My initial approach for doing this is to release tagged
versions of our base package. To release an installable component, we're going
to leverage the gitlab CI pipeline and gitlab API to pull what would amount to
our example project from the upstream repo at the versio number that we want,
extract the particular component we want to package and publish a release to
our pypi package registry.

[Creating a release job](https://docs.gitlab.com/ee/user/project/releases/#create-a-release-by-using-a-cicd-job)
is well documented in the gitlab docs. It's fairly trivial to set up the
django-base repository to create a release each time we push a tag to remote
origin.
