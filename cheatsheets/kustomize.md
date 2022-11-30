kustomize
=========

## Another deployment tool ##

urgh...
It's like make but /less|more/ confusing ;-)

## Basic project structure

Generally, the most basic setup for a project will take the following
structure: 

```
cloudstream-infra/
├── deployment.yaml
├── kustomization.yaml
├── README.md
└── service.yaml

0 directories, 4 files
```

### see what this generates

```
kustomize build ~/cloudstream-infra
```


### patch this into openshift

```
kustomize build ~/cloudstream-infra | oc apply -f -
```

### Open questions

1. what is the relationship between the names used for metadata, labels and 
   selectors in the kustomize yaml files and the oc project that we are working on?
