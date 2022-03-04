workflow for argocd
===================

(https://application-gitops-server-application-gitops.apps.dev-ocp1.nw.mdw.ac.at/login?return_url=https%3A%2F%2Fapplication-gitops-server-application-gitops.apps.dev-ocp1.nw.mdw.ac.at%2Fapplications%3Fproj%3D%26sync%3D%26health%3D%26namespace%3D%26cluster%3D%26labels%3D)

+ initial directory structure for deployment of a test django app on openshift.

```
mkdir -p base/{deployments,secrets,services} overlays/{development,staging}

.
├── base
│   ├── deployments
│   ├── secrets
│   └── services
├── overlays
│   ├── development
│   └── staging
└── README.md
```


