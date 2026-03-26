做一个PPT翻译的网站，用户上传PPT后，调用大模型进行翻译保持格式不变。不过是不是实时处理的，是一个任务提交型，排队任务处理，用户在翻译的时候可以填写自己的姓名，然后可以查找自己姓名下面的任务状态，可以删除任务，
大模型调用的样例：curl https://api.apiyi.com/v1/chat/completions
-H "Content-Type: application/json"
-H "Authorization: Bearer sk-W42q0xKL8hew5mkE360296F630724474B0Cf4355F1762cF7"
-d '{
"model": "gpt-4o-mini",
"stream": false,
"messages": [
{
"role": "system",
"content": "You are a helpful assistant."
},
{
"role": "user",
"content": "Hello!"
}
]
}'