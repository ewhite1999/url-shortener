import React from "react";

const Search = () => {
  return (
    <>
      <h1 className="border-black border-4">URL Shortener</h1>
      <h3>Shorten your URL for FREE by pasting link in box below</h3>
      <form>
        <label for="url">Enter Link</label>
        <input type="input" id="url" name="url" placeholder="Paste Link Here" />
        <input type="submit" />
      </form>
    </>
  );
};
export default Search;
