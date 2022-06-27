import { useSWRConfig } from "swr";
import { useRouter } from "next/router";
import Column from "../../components/column";
import Spinner from "../../components/spinner";
import Error from "../../components/error";
import Attributes from "../../components/attributes";
import Ago from "../../components/ago";
import useEntity from "../../hooks/entity";

function Starship({ url }) {
  const { data, isLoading, isError } = useEntity({ url, sendRequest: true });
  if (isLoading) return <Spinner />;
  if (isError) return <Error />;
  return <div>{data.name}</div>;
}

function Film({ url }) {
  const { data, isLoading, isError } = useEntity({ url, sendRequest: true });
  if (isLoading) return <Spinner />;
  if (isError) return <Error />;
  return <div>{data.title}</div>;
}

function Person() {
  const attrMap = {
    name: "Name",
    height: "Height",
    mass: "Mass",
    hair_color: "Hair Color",
    skin_color: "Skin Color",
    eye_color: "Eye Color",
    birth_year: "Birth Year",
    gender: "Gender",
  };
  const router = useRouter();
  const { id } = router.query;
  const url = `https://swapi.dev/api/people/${id}`;
  const sendRequest = id >= 0 && id !== null;
  const current = new Date();
  const { data, isLoading, isError } = useEntity({ url, sendRequest });
  if (isLoading) return <Spinner />;
  if (isError) return <Error />;
  if (data) {
    return (
      <div className="aligner aligner-vertical">
        <h1>{data.name}</h1>
        <Ago
          text="Last Updated"
          timeInThePast={data.edited}
          current={current}
        />
        <h2>Attributes</h2>
        <ul>
          <Attributes obj={data} mapping={attrMap} />
        </ul>
        <h2>Starships Flown</h2>
        <ul>
          {data.starships.map((s) => (
            <Starship key={s} url={s} />
          ))}
        </ul>
        <h2>Films</h2>
        <ul>
          {data.films.map((s) => (
            <Film key={s} url={s} />
          ))}
        </ul>
      </div>
    );
  }
}

export default function People() {
  return (
    <div className="columns">
      <Column position="centered">
        <Person />
      </Column>
    </div>
  );
}
