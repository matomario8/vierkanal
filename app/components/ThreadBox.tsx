import { SERVER_PROPS_ID } from 'next/dist/shared/lib/constants';
import Link from 'next/link'
import Image from 'next/image'
import React from "react";

type Thread = {
  id: string
  title: string
  comment: string
}

export default class ThreadBox extends React.Component<Thread> {


  render() {
    return (<div className="flex flex-col w-52">
      <span>{this.props.id}</span>
      <Image alt="post-image" className="w-100 h-100" src="https://picsum.photos/100/100" width="100" height="100"></Image>
      <span className="font-semibold">{this.props.title}</span>
      <span className="font-light">{this.props.comment}</span>
    </div>)
  }
}
