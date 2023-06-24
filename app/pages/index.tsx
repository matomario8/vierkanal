import Link from 'next/link'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import { useState } from 'react'

const inter = Inter({ subsets: ['latin'] })



const Home = () => {
  const [board, setBoard] = useState("");

  return (
    <main
      className={`flex min-h-screen flex-col items-center p-24 ${inter.className}`}
    >
      
      <Header title="Home" imgUrl="/assets/bildschirmfoto.png"></Header>

      <Link href="/catalog">/g/</Link>
      
    </main>
  )
}

export default Home;
