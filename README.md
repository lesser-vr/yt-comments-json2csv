# YouTube comments json to csv
유튜브 댓글 추첨용 yt-dlp의 json을 csv로 변환하는 간단한 python 프로그램

* author는 중복 가능이라 아래 규칙의 `author_and_id` 값을 새로 조합
  * `author`의 첫번째 캐릭터는 항상 @라서 제외
  * `author_id`의 마지막 5글자를 `@` 구분자로 조합
* csv 파일을 엑셀로 읽어서 `author_and_id`를 [marble roulette](https://lazygyu.github.io/roulette/)에 넣어서 추첨
* 너무 많으면 시간이 오래 걸리기 때문에 엑셀에서 랜덤으로 일정 수 뽑아서 하는 것 추천
  * e.g. `=INDEX($A$2:$A$1000, RANDBETWEEN(2, 1000))`

## input
* yt-dlp's comments array json
* e.g. `yt-dlp --write-comments --skip-download {YOUTUBE_URL} | jq '.comments' > comments.json`
* json example
```json
[
    {
      "id": "UgyxXhs9QHs7whJ0aXJ4AaABAg",
      "text": "This video was really informative, thank you!",
      "author": "John Doe",
      "author_id": "UCXXXXX",
      "author_thumbnail": "https://yt3.ggpht.com/a/AATXAJzSfsA1...",
      "likes": 15,
      "heart": false,
      "is_favorited": false,
      "is_pinned": false,
      "time_text": "1 day ago",
      "timestamp": 1662105600
    },
    {
      "id": "UgzwtnbeU97zL6rU7EB4AaABAg",
      "text": "I learned a lot from this, thanks!",
      "author": "Jane Smith",
      "author_id": "UCYYYYY",
      "author_thumbnail": "https://yt3.ggpht.com/a/AATXAJwJ...",
      "likes": 5,
      "heart": true,
      "is_favorited": false,
      "is_pinned": true,
      "time_text": "2 days ago",
      "timestamp": 1662029200
    }
]
```

## output
* e.g. `python -m json2csv`
* csv sample
```
author_and_id,comment_id,text,likes,time_text,is_reply
@씨브려보소@UC4quSr3Xu0K6eqHJ0eP9KnA,UgyNfcEqRGvxvdL_och4AaABAg.A8fXyC1PACnA8gEqcvjjK6,메타도 트래커 만들어 주라~~~,0,,False
@gauntlet84@UC99_0SEl82cWpOSrSHoOCjg,UgyNfcEqRGvxvdL_och4AaABAg.A8fXyC1PACnA8gFgZ8S1pr,구독 진즉에 했는데유 ㅋㅋㅋ 주세요! ㅋㅋㅋ,0,,False
@grocks7195@UC-KS8s8XbLO8Ks3wa83qp6A,UgyNfcEqRGvxvdL_och4AaABAg.A8fXyC1PACnA8gFishvo29,피코 좋아보이네요,0,,False
```