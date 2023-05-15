import { Component } from 'react'
import useState from 'react'

export default class NewThread extends Component {

  state = {
    threadTitle: "",
    threadText: ""
  }

  //Add a name and options field
  render() {

    return (
      <div class="border-gray-300 border-2 my-8 p-2">
        <p className="font-semibold">New Thread</p>
        
        <p>Subject</p>
        <input value={this.state.threadTitle}
                onChange={e => this.setState({threadTitle: e.target.value})}>
        </input>
        <p>Text</p>
        <textarea value={this.state.threadText}
                  onChange={e => this.setState({threadText: e.target.value})}
                  className="w-full md:max-w-5xl">
        </textarea><br />
        <button class="bg-blue-800 hover:bg-blue-700 text-white font-bold py-1 px-4 rounded">Submit</button>

      </div>
    )
  }
}