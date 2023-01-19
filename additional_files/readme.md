After adding the new font, you may need update the font cache and remove the matplotlib font cache:
```
sudo fc-cache -fv
rm -fr ~/.cache/matplotlib
```
