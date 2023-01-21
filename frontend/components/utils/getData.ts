import axios from "axios";

const baseUrl = `${process.env.NEXT_PUBLIC_BACKEND_URL}/`;

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

export async function getCode(endpoint: string) {
  const url = baseUrl + endpoint;
  const result = await axios.get(url)
  return result.data
}