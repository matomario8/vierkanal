import Link from 'next/link'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import { useState } from 'react'

const inter = Inter({ subsets: ['latin'] })

const Home = () => {

  return (
    <main
      className={`flex min-h-screen flex-col items-center p-24 ${inter.className}`}
    >
      
      <Header title="Home" imgUrl=""></Header>

      <div className="grid grid-cols-4 w-full mt-8 text-center">
        <div className="col">
          <span>Video Games</span>
          <ul>
            <li>Video Games</li>
            <li>Video Game Generals</li>
            <li>Video Games/Multiplayer</li>
            <li>Video Games/Mobile</li>
          </ul>
        </div>
        <div className="col">
          <span>Interests</span>
          <ul>
            <li>Technology</li>
            <li>Sports</li>
            <li>Television</li>
            <li>International</li>
          </ul>
        </div>
        <div className="col">
          <span>Creative</span>
          <ul>
            <li>Photography</li>
            <li>Art</li>
            <li>Music</li>
            <li>Literature</li>
          </ul>
        </div>
        <div className="col">
          <span>Other</span>
          <ul>
            <li>Business</li>
            <li>Travel</li>
            <li>Fitness</li>
            <li>Current News</li>
          </ul>
        </div>
      </div>
    </main>
  )
}

export default Home;
