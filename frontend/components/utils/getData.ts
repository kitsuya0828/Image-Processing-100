import axios from "axios";

const baseUrl = "http://localhost:8000/";

export async function postData(endpoint: string, file: FormData) {
  const url = baseUrl + endpoint;
  const result = await axios
    .post(url, file, {
      headers: {
        "content-type": "multipart/form-data"
      }
    })
    .then((response) => {
        // console.log(response)
        return response
    });
    return result.data
}
