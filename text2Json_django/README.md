# This is the django part of the text2knowledgeGraph repo

## Key Idea 

Create APIs, which will be called by the React part of the code

## To run the server, install django and then : 

```
python manage.py runserver
```

## Test API Calls based on this 

To setup do : `OPENAI_API_KEY=sk-your-openai-key` on the terminal.

There are roughly 2 base use case APIs this repo creates :

1. Text -> Initial JSON -> HTML from JSON2Tree
Request Type = `POST`
url = `http://127.0.0.1:8000/api/create-graph-from-text/`
example body = ```{"text":"The French Revolution[a] was a period of political and societal change in France that began with the Estates General of 1789, and ended with the coup of 18 Brumaire on November 1799 and the formation of the French Consulate. Many of its ideas are considered fundamental principles of liberal democracy,[1] while its values and institutions remain central to modern French political discourse.The causes are generally agreed to be a combination of social, political and economic factors, which the Ancien Régime proved unable to manage. A financial crisis and widespread social distress led, in May 1789, to the convocation of the Estates General which was converted into a National Assembly in June. The Storming of the Bastille on 14 July led to a series of radical measures by the Assembly, among them the abolition of feudalism, state control over the Catholic Church in France, and a declaration of rights.The next three years were dominated by the struggle for political control, exacerbated by economic depression."}```

2. Text + Previous JSON -> Updated JSON -> HTML from JSON2Tree
Request Type = `POST`
url = `http://127.0.0.1:8000/api/add-to-graph-from-text/`
example body = ```{"text":"The French Revolution[a] was a period of political and societal change in France that began with the Estates General of 1789, and ended with the coup of 18 Brumaire on November 1799 and the formation of the French Consulate. Many of its ideas are considered fundamental principles of liberal democracy,[1] while its values and institutions remain central to modern French political discourse.The causes are generally agreed to be a combination of social, political and economic factors, which the Ancien Régime proved unable to manage. A financial crisis and widespread social distress led, in May 1789, to the convocation of the Estates General which was converted into a National Assembly in June. The Storming of the Bastille on 14 July led to a series of radical measures by the Assembly, among them the abolition of feudalism, state control over the Catholic Church in France, and a declaration of rights.The next three years were dominated by the struggle for political control, exacerbated by economic depression.", "json_text" = {}}```

More to be added soon ......