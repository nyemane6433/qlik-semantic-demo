exports = async function(changeEvent) {

  // Access the _id of the changed document:
  const docId = changeEvent.documentKey._id;

  const serviceName = "mongodb-atlas";
  const database = "qlik";
  const collection = context.services(serviceName).db(database).collection('test');
  
  const url = 'https://api.voyageai.com/v1/embeddings';
  const voyageapi_key = context.values.get("voyageapi_key");

  // Get the "FullDocument" present in the Insert/Replace/Update ChangeEvents
  try {

    // If this is an "insert", "update", or "replace" event
    if (changeEvent.operationType === "insert" || changeEvent.operationType === "update" || changeEvent.operationType === "replace") {

      let response = await context.http.post({
          url: url,
           headers: {
              'Authorization': [`Bearer ${voyageapi_key}`],
              'Content-Type': ['application/json']
          },
          body: JSON.stringify({
              
              input: doc.description,
              model: context.values.get("voyage_model")
          })
      });
              
      let responseData = EJSON.parse(response.body.text());
      if(response.statusCode === 200) {
        console.log("Successfully received embedding.");
        const embedding = responseData.data[0].embedding;
        const result = await collection.updateOne({ _id: docId },{ $set: { description_embedding: embedding }});
        
        if(result.modifiedCount === 1) {
          console.log("Successfully updated the document.");
        } else {
          console.log("Failed to update the document.");
        }
      } else {
        console.log(`Failed to receive embedding. Status code: ${response.statusCode}`);
      }
  }

  }catch(err) {
    console.log("error performing mongodb write: ", err.message);
  }
};