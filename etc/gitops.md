some notes on gitops tools with openshift
=========================================

# Argo CD

You can set up various code and infrastructure repositories in git, then simply
give the git url when creating a new app with argo cd. Argo will do the rest
... i.e. it carries out the deployment specified in the repo. 

## argocd url

(https://application-gitops-server-application-gitops.apps.dev-ocp1.nw.mdw.ac.at/login?return_url=https%3A%2F%2Fapplication-gitops-server-application-gitops.apps.dev-ocp1.nw.mdw.ac.at%2Fapplications)

## gitops-tree

```
.
├── bootstrap
│   └── gitops
│       ├── base
│       │   ├── kustomization.yaml
│       │   └── openshift-gitops-operator-subscription.yaml
│       └── overlays
│           ├── cluster-admin
│           │   ├── cluster-admin-rolebinding.yaml
│           │   ├── cluster-admins-group.yaml
│           │   └── kustomization.yaml
│           └── default
│               └── kustomization.yaml
├── components
│   ├── apps
│   │   └── application-gitops
│   │       └── base
│   │           ├── application-admins-group.yaml
│   │           ├── application-gitops-argocd.yaml
│   │           ├── kustomization.yaml
│   │           └── namespace.yaml
│   ├── argocd
│   │   └── apps
│   │       ├── application-gitops
│   │       │   └── base
│   │       │       ├── application-gitops-application.yaml
│   │       │       └── kustomization.yaml
│   │       ├── bootstrap
│   │       │   └── base
│   │       │       ├── bootstrap-application.yaml
│   │       │       └── kustomization.yaml
│   │       └── openshift-gitops
│   │           └── base
│   │               ├── kustomization.yaml
│   │               └── openshift-gitops-application.yaml
│   └── configuration
│       └── openshift-gitops
│           └── base
│               ├── kustomization.yaml
│               └── openshift-gitops-argocd.yaml
├── gitops-tree.txt
└── README.md

```




# Kustomize

As mentioned on the website, kustomize is a tool whose functionality is
somewhere in between make and sed. In the sense that it is a build tool and a
stream editor i.e. something that emits text.

```
Dev ---->  Gitlab  <------- Ops
             |
             |
             v
           GitOps --> Kustomize
             |
             v
          OpenShift
```


Overview of a kustomize file,
[Kustomize API](https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/)


Kustomize generally works with *base* templates and *overlays*. 


## Patches

Generally speaking, we are often using generators (which are interfaces) to
generate patches for existing yaml files. All of this is done through yaml
files called **overlays**. 

Typical workflow is to define placeholders called `pathcme` in the base yaml
that needs to be patched. The overlay then describes in yaml format the type of
generator that is to be created. Basically a trio of: 

```
op: ...
path: ...
value: ...
```

## Build command

```
kustomize build /path/to/overlay | oc apply -f -
```

## Namespace type things...

```
.
├── dev
│   ├── base
│   │   ├── kustomization.yaml
│   │   └── namespace.yaml
│   ├── overlays
│   │   ├── mdw-test-namespace
│   │   │   └── kustomization.yaml
│   │   └── mdw-test-workshop
│   │       └── kustomization.yaml
│   └── README.md
├── prod
│   └── README.md
├── README.md
└── test
    └── README.md
```



# Typical workflows

There seems to be a pattern that recurs frequenctly enough, that is to run some
command using `oc` and to save the output to a yaml file. 

```
oc adm policy add rolebinding ...
oc get rolebindings -oyaml admin > admin-rolebinding.yaml
```
