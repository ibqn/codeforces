## Locate binary files

```shell
 find . -type f ! -size 0 -exec grep -IL . "{}" \;
```
