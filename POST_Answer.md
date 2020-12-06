### REST Api Answer
Some answer on document are removed accidentally, so i just post it on this answer repository 

**POST**
**Do**
 - When user input data on form / web forms, because is more secure than GET since is not exposed to url address bar and can held more data.
 - Used for update data on server.

**Don't**
- Don’t used POST on repeatable request or cached request.
- Don't used POST on anything, you should used only UPDATE, DELETE, PUT request if these API only to get data, update data or remove data.

**GET**
**Do**
- When for calling repeatable or cacheable request which use less data to get, and visible to user so can be bookmarked by user.

**Don't**
- Don't used on sensitive data, because it will exposed to user.
- Don't used long data, because it have limit.
 