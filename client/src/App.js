import React from "react";
import axios from "axios";
// import { Switch, Route } from 'react-router-dom';

import { Search } from "./components";

const App = () => {
  const handleLoad = async () => {
    const url = location.href;
    const param = url.split("8080/")[1];
    try {
      const res = await axios.get(`http://127.0.0.1:5000/${param}`);
      if (res.status === 200) {
        const long_url = res.data.long_url;
        if (long_url) location.href = long_url;
      }
    } catch {
      alert("We don't have that url yet, try making one!");
      location.href = "http://localhost:8080/";
    }
  };
  window.onload = handleLoad();

  return (
    <>
      <Search />
    </>
  );
};

export default App;
