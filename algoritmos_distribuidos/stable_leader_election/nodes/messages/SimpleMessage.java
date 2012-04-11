package projects.stable_leader_election.nodes.messages;

import sinalgo.nodes.messages.Message;

public class SimpleMessage extends Message {

	public String data;

	public SimpleMessage(String data) {
		this.data = data;
	}

	@Override
	public Message clone() {
		return this;
	}

}
