import Link from 'next/link'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import { useState } from 'react'

const inter = Inter({ subsets: ['latin'] })

const [board, setBoard] = useState("")

const Home = () => {
  return (
    <main
      className={`flex min-h-screen flex-col items-center p-24 ${inter.className}`}
    >
      
      <Header title="Technology" imgUrl="/assets/bildschirmfoto.png"></Header>

      <Link href="/technology">/g/</Link>
      
    </main>
  )
}

export default Home;
