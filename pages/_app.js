import Head from "next/head";
import { SWRConfig } from "swr";
import "../styles/globals.css";
import Header from "../components/header";
import Footer from "../components/footer";

function MyApp({ Component, pageProps }) {
  return (
    <div className="container">
      <Head>
        <title>Corinth Code</title>
        <meta name="description" content="Corinth Web App" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Header />
      <SWRConfig
        value={{
          fetcher: (...args) => fetch(...args).then((res) => res.json()),
        }}
      >
        <main>
          <Component {...pageProps} />
        </main>
      </SWRConfig>
      <Footer />
    </div>
  );
}

export default MyApp;
