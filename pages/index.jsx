import { useState, useCallback } from "react";
import useSWR from "swr";
import Link from "next/link";
import Column from "../components/column";
import Spinner from "../components/spinner";
import Error from "../components/error";
import Attributes from "../components/attributes";
import Ago from "../components/ago";
import Result from "../components/result";
import useEntity from "../hooks/entity";

function Search() {
  const [searchInput, setSearchInput] = useState("");

  const handleChange = (value) => {
    setSearchInput(value);
  };

  return (
    <>
      <div className="empty">
        <div className="empty-icon">
          <i className="icon icon-3x icon-search"></i>
        </div>
        <p className="empty-title h5">Search for Your Favorite</p>
        <div className="empty-action input-group input-inline">
          <input
            className="form-input"
            type="text"
            placeholder="What is wookie?"
            onChange={(e) => handleChange(e.target.value)}
            value={searchInput}
          />
          <button className="btn btn-primary input-group-btn">Search</button>
        </div>
      </div>
      <Results q={searchInput} />
    </>
  );
}

function Results({ q }) {
  const sendRequest = q != "";
  const { data, isLoading, isError } = useEntity({ q, sendRequest });
  if (isLoading && sendRequest) return <Spinner />;
  if (isError) return <Error />;
  if (!data) return <></>;
  const results = data.results.filter((person) => {
    return person.name.toLowerCase().includes(q.toLowerCase());
  });
  return (
    <div className="aligner aligner-vertical">
      {results &&
        results.map((person) => (
          <Result
            key={person.name}
            title={person.name}
            obj={person}
            id={person.url.split("/").slice(-2)[0]}
          />
        ))}
    </div>
  );
}

export default function Landing() {
  return (
    <div role="landing" className="columns">
      <Column position="centered">
        <Search />
      </Column>
    </div>
  );
}
