import useSWR, { useSWRConfig } from "swr";

export default function useEntity(params) {
  const { url, q, sendRequest } = params;
  const uri = url ? url : `https://swapi.dev/api/people/?search=${q}`;
  const { data, error } = useSWR(sendRequest ? uri : null);

  return {
    data: data,
    isLoading: !error && !data,
    isError: error,
  };
}
