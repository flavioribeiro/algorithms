package projects.stable_leader_election.nodes.messages;

import sinalgo.nodes.messages.Message;

/**
 * The Messages that are sent by the S1Nodes in the Sample1 projects. They contain one int
 * as payload.
 */
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
