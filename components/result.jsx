import Link from "next/link";
import { get_subtitle, get_initial, get_url } from "../utils/text";

export default function Result({ title = "", obj, id }) {
  obj.type = "people";
  return (
    <div role="result" className="tile tile-centered">
      <div className="tile-icon">
        <figure
          className="avatar bg-primary"
          data-initial={get_initial(obj)}
        ></figure>
      </div>
      <div className="tile-content">
        <p className="tile-title">
          <Link href={get_url(obj)}>{title}</Link>
        </p>
        <p className="tile-subtitle">{get_subtitle(obj)}</p>
      </div>
    </div>
  );
}
