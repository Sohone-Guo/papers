删除GIt
```bash
git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch filename" --prune-empty --tag-name-filter cat -- --all

  

git push origin --force --all  
git push origin --force --tags
```