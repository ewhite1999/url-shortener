import React, { useState } from "react";
import axios from "axios";

const Search = () => {
  const [shortURL, setShortURL] = useState("");
  const [longURL, setLongURL] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = e.target.url.value;
    setLongURL(url);

    const data = { long_url: url };
    const extra = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const result = await axios.post("http://127.0.0.1:5000/urls", data, extra);
    const responseData = result.data;
    const message = responseData.message;

    if (message) setMessage(message);
    setShortURL(`http://localhost:8080/${responseData.short_url}`);
    e.target.reset();
  };
  return (
    <>
      <h1 className="text-4xl text-center pb-4 mt-8">URL Shortener</h1>
      <h3 className="text-2xl text-center pb-4">
        Shorten your URL for FREE by pasting link in box below
      </h3>
      <form onSubmit={handleSubmit} className="flex flex-col max-w-xl mx-auto">
        <div className="flex space-x-2">
          <label htmlFor="url" className="p-2">
            Enter Link:
          </label>
          <input
            type="input"
            id="url"
            name="url"
            placeholder="Paste Link Here"
            className="border-b-2 w-96 p-2"
          />
        </div>
        <input
          type="submit"
          className="mt-8 py-2 px-4 bg-slate-400 text-slate-900 mx-auto"
        />
      </form>
      <div className="flex flex-col max-w-xl mx-auto space-y-2 mt-4">
        {message && <p>We already processed that url, here you go</p>}
        {longURL && (
          <a className=" text-blue-700 hover:text-blue-300" href={longURL}>
            Long URL: {longURL}
          </a>
        )}
        {shortURL && (
          <a className=" text-blue-700 hover:text-blue-300" href={shortURL}>
            Short URL: {shortURL}
          </a>
        )}
      </div>
    </>
  );
};
export default Search;
