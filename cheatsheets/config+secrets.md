# config maps

```
oc apply -f my-configmap.yaml
```

# sealed secrets with bitnami

## Getting started with sealed secrets

From the binami docs:

```
# Create a json/yaml-encoded Secret somehow:
# (note use of `--dry-run` - this is just a local file!)
echo -n bar | kubectl create secret generic mysecret --dry-run=client --from-file=foo=/dev/stdin -o json >mysecret.json
```

Adapted for our purposes:

```
oc create secret generic base-secret --dry-run=client --from-env-file=.env -o yaml >base-secret.yaml
```

to transform this into a sealed secret that can be stored in git:

```
kubeseal -o yaml <base-secret.yaml >base-sealedsecret.yaml
```

to upload the sealed secret to openshift:

```
oc create -f base-sealedsecret.yaml
```

get the secret:

```
oc get secret base-sealedsecret.yaml
```

# Using config maps and secrets
