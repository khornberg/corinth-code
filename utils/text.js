function person_subtitle(person) {
  return `Starships: ${person.starships.length} — Films: ${person.films.length}`;
}

export function get_subtitle(obj) {
  const subtitles = {
    people: person_subtitle,
  };
  if (subtitles[obj.type]) {
    return subtitles[obj.type](obj);
  }
  return obj.type;
}

export function get_initial(obj) {
  return obj.name
    ? `${obj.name.substring(0, 2)}`
    : `${obj.title.substring(0, 2)}`;
}

export function get_url(obj) {
  const id = obj.url.split("/")[5];
  return `/${obj.type}/${id}`;
}
