import html
texto = html.escape("this html fragment contains a <script>script</script> tag.")
texto2 = html.unescape("I &hearts; Python´s &alt;standard library&gt;.")
print(texto)
print(texto2)