import algoliasearch from "algoliasearch/lite";
import {
  InstantSearch,
  SearchBox,
  Hits,
  Highlight,
  RefinementList,
  Pagination,
  Configure,
} from "react-instantsearch-hooks-web";
import Link from "next/link";
import { get_subtitle, get_initial, get_url } from "../utils/text";

const searchClient = algoliasearch(
  "8H44TT0Z6X",
  "c087744b8365f9b4e2af066126c5443b"
);

function Hit({ hit }) {
  const highlightAttr = hit.name ? "name" : "title";
  return (
    <div role="result" className="tile tile-centered">
      <div className="tile-icon">
        <figure
          className="avatar bg-primary"
          data-initial={get_initial(hit)}
        ></figure>
      </div>
      <div className="tile-content">
        <p className="tile-title">
          <Link href={get_url(hit)}>
            <Highlight attribute={highlightAttr} hit={hit} />
          </Link>
        </p>
        <p className="tile-subtitle">{get_subtitle(hit)}</p>
      </div>
    </div>
  );
}

export default function Advanced() {
  return (
    <div className="advanced-search-container">
      <InstantSearch searchClient={searchClient} indexName="corinth">
        <Configure hitsPerPage={10} />
        <RefinementList attribute="type" className="advanced-search-filters" />
        <div className="advanced-search-area">
          <SearchBox />
          <Hits hitComponent={Hit} className={"hits"} />
          <Pagination />
        </div>
      </InstantSearch>
    </div>
  );
}
