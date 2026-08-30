def apply(legacy):
    patch = r'''<style>
/* Keep the right/side main navigation visible while the long table scrolls. */
.side{
  position:sticky;
  top:18px;
  align-self:start;
  max-height:calc(100vh - 36px);
  overflow:visible;
}
@media(max-width:720px){
  .side{top:10px;max-height:calc(100vh - 20px)}
}
</style>'''
    legacy.HTML = legacy.HTML.replace('</head>', patch + '</head>')
