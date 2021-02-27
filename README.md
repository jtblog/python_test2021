# NOTE
<hr>

### alt.py contains an alternative code
Return strings only as responses. Any request gets any of these responses <br>
*   "Action is successful: 200 Ok"
*   "The request is invalid: 400 bad request"
*   "Any error: 500 internal server error"

### app.py on the other hand 
Return json objects as responses and not just strings <br>
e.g. Any of the POST, PUT and DELETE request gets json responses like this
```json
{
    "audioFileID" : 1222,
    "audioFileType" : "mime"
}
```
while GET request get json responses like those of the 
body formats represented at the bottom of this markdown <br>

<br>
To use alt.py <br>
Set the current flask app to alt.py <br>
Run the command <br>

```bash
> set FLASK_APP=alt.py
```
```bash
> flask run
```

and viz a viz <br>
i.e. You can reset the current flask app to app.py again by running <br>

```bash
    > set FLASK_APP=app.py
```
```bash
    > flask run
```

<hr>

## Endpoints
<br>

```bash
*   "/api/create"   --  method = POST
*   "/api/delete/<audioFileType>/<audioFileID>" --  method = DELETE
*   "/api/update/<audioFileType>/<audioFileID>" --  method = PUT:
*   "/api/get/<audioFileType>"  --  method = GET
*   "/api/get/<audioFileType>/<audioFileID>"    --  method = GET
```

<hr>

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
<hr>

# Thank you
