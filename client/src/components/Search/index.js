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
      <h1 className="border-black border-4">URL Shortener</h1>
      <h3>Shorten your URL for FREE by pasting link in box below</h3>
      <form onSubmit={handleSubmit}>
        <label htmlFor="url">Enter Link</label>
        <input type="input" id="url" name="url" placeholder="Paste Link Here" />
        <input type="submit" />
      </form>
      <div>
        {message && <p>We already processed that url, here you go</p>}
        <a href={longURL}>Long URL: {longURL}</a>
        <a href={shortURL}>Short URL: {shortURL}</a>
      </div>
    </>
  );
};
export default Search;
