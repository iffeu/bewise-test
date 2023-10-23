# Instructions
## How to run
`docker compose up --build` \
This will run the server at `http://localhost:8000/`

## Example of the POST request
Send this request from `http://localhost:8000/questions/` using Chrome console \
```fetch('', {
  method: 'POST',
  body: JSON.stringify({
    questions_num: 3,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json)); ```
