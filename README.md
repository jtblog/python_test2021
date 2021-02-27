# NOTE
__________________________ <br>
alt.py contains an alternative code <br>
Return strings only as responses. Any of 
*   "Action is successful: 200 Ok"
*   "The request is invalid: 400 bad request"
*   "Any error: 500 internal server error"

app.py on the other hand
Return json objects as responses and not just strings

To use alt.py <br>
<br>
Set the current flask app to alt.py <br>
Run the command
```bash
> set FLASK_APP=alt.py
```
```bash
> flask run
```

and viz a viz <br>
i.e. You can reset the current flask app to app.py again by running
```bash
> set FLASK_APP=app.py
```
```bash
> flask run
```

__________________________ <br>
## Endpoints
<br>
*   '/api/create'   --  method = POST
*   '/api/delete/<audioFileType>/<audioFileID>' --  method = DELETE
*   '/api/update/<audioFileType>/<audioFileID>' --  method = PUT
*   '/api/get/<audioFileType>'  --  method = GET
*   '/api/get/<audioFileType>/<audioFileID>'    --  method = GET

__________________________ <br>
## Body format
### Song:
```json
{
    "audioFileType" : "mime",
    "audioFileMetadata" : {
        "id" : 1222,
        "name" : "Name of songs",
        "duration" : 56,
        "upload_time" : "Time of upload (DateTime)",
        "participants" : "List of participants"
    }
}
```

### Podcast:
```json
{
    "audioFileType" : "mime",
    "audioFileMetadata" : {
        "id" : 1222,
        "name" : "Name of podcast",
        "duration" : 56,
        "upload_time" : "Time of upload (DateTime)",
        "host" : "Name of host",
        "participants" : ["Name of participant1", "Name of participant2", "..."]
    }
}
```

### Audiobook:
```json
{
    "audioFileType" : "mime",
    "audioFileMetadata" : {
        "id" : 1222,
        "name" : "Title of audiobook",
        "duration" : 56,
        "upload_time" : "Time of upload (DateTime)",
        "author" : "Author of the title",
        "narrator" : "Narrator"
    }
}
```
__________________________ <br>
# Thank you