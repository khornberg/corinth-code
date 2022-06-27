import Image from "next/image";
import Link from "next/link";
import styles from "../styles/App.module.css";

export default function Header() {
  return (
    <header className="navbar">
      <section className="navbar-section">
        <span className="btn btn-link">
          <Link href="/">Home</Link>
        </span>
        <span className="btn btn-link">
          <Link className="btn btn-link" href="/advanced">
            Advanced
          </Link>
        </span>
      </section>
      <section className="navbar-center">
        <Image
          src="/Corinth.png"
          width="100px"
          height="100px"
          alt="corinth"
          className={styles.header_logo}
        />
      </section>
      <section className="navbar-section">
        <a
          href="https://github.com/khornberg/corinth-code"
          className="btn btn-link"
        >
          GitHub
        </a>
      </section>
    </header>
  );
}
