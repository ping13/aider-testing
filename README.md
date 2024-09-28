# Log

This is the log of my first test with Aider

### Initiate this project

```
uv init aider-testing
uv add --dev aider-chat
```

### Add key to `.env`

```
ANTHROPIC_API_KEY=sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Start `aider`

```
uv run aider
```

It will ask to create a git repository, which is nice


### Create a game of pong


> - /HELP
> - /help

Okay, asking for help needs some practice ☺️.

I started by following the [example chat for creating a Pong
game](https://aider.chat/examples/pong.html)

> - can you make a simple game of pong with pygame?  
> - go ahead  
> - the ball moves too fast  
> - The paddles need to be bigger and with different colors.  
> - Can you run the shell command with `uv run python` instead of `python`?

Then I wanted to try some of my own experiments:

> - Can you ask for the name of the player prior to the start and show the initial on the paddle?  
> - Can you make the paddle movve faster?  
> - Can you make the paddle faster the longer you press the key? Like every 0.2 secs 20% faster  
> - Make the computer player miss the ball randomly like every 10 times  
> - If the player types multiple words for her name, use all the initial for each word  
> - /help  
> - /ask how many lines of code  
> - /lint  
> - /models  
> - /ls  
> - /diff  
> - /help  
> - /tokens

Full transcipt is [here](./aider-chat-pong.md).

### Final result

![Entry page](./img/screenshot_start.png)

![Play mode](./img/screenshot_game.png)


#### Costs

```
Approximate context window usage for claude-3-5-sonnet-20240620, in tokens:  
$ 0.0052    1,735 system messages  
$ 0.0062    2,065 chat history    use /clear to clear  
$ 0.0052    1,727 pong.py         /drop to remove  
==================  
$ 0.0166    5,527 tokens total  
194,473 tokens remaining in context window  
200,000 tokens max context window size  
```



