# 🔧 Troubleshooting

## Reducing Git Size

To remove large files from a Git repo use [**BFG**](https://rtyley.github.io/bfg-repo-cleaner/).

```bash
brew install bfg
```

```bash
git clone --mirror git://example.com/some-big-repo.git
```

```bash
bfg --strip-blobs-bigger-than 1M some-big-repo.git 
```

```bash
# Now remove the untracked data
cd some-big-repo.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git push
```
