import React from 'react';
import { useState } from 'react';
import axios from 'axios';

const Search = ({ url }) => {
	const [shortURL, setShortURL] = useState('');
	const [longURL, setLongURL] = useState('');

  const handleInput = (e) => {
    setLongURL(e.target.value)
  }

	const fetchURL = async (e) => {
		e.preventDefault();
   
		await fetch('http://127.0.0.1:5000/urls/', {
			method: 'POST',
      // mode: 'no-cors',
			body: JSON.stringify(longURL),
      headers: { "Content-Type": "application/json" },
		})
			.then((res) => res.json())
			.then((data) => {
        // console.log(data);
				setShortURL(data.url.short_url);
				setLongURL(data.url.long_url);
			});
	};

	return (
		<>
			<h1 className="border-black border-4">URL Shortener</h1>
			<h3>Shorten your URL for FREE by pasting link in box below</h3>
			<form onSubmit={(e) => fetchURL(e)}>
				<label htmlFor="url">Enter Link</label>
				<input
					type="input"
					value={longURL}
					id="url"
					name="url"
					placeholder="Paste Link Here"
					onChange={handleInput}
				/>
				<input type="submit" />
			</form>
      <div>
        <p>Long URL: {longURL}</p>
        <p>Short URL: {shortURL}</p>
      </div>
		</>
	);
};
export default Search;
