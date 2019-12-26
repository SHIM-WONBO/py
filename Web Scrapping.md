# Web Scrapping

---

`requests`  pachage를 import해야 한다.

`value = request.get("https://fora22.github.io")`

`request.get`  함수를 사용하면 해당 URL에 있는 html 정보를 다 가져올 수 있다.

`value.text` 하면 text 정보만, `value.json` 정보만, `value.headers`하면