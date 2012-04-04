package projects.stable_leader_election.nodes.timers;

import sinalgo.nodes.Node;
import sinalgo.nodes.messages.Message;
import sinalgo.nodes.timers.Timer;
import sinalgo.tools.logging.Logging;


public class MyMessageTimer extends Timer {
	private Node receiver; // the receiver of the message, null if the message should be broadcast
	private Message msg; // the message to be sent
	
	Logging log = Logging.getLogger("stable_election_log");

	public MyMessageTimer(Message msg, Node receiver) {
		this.msg = msg;
		this.receiver = receiver;
	}

	public MyMessageTimer(Message msg) {
		this.msg = msg;
        log.logln("opa sou um timer de broadcast");
		this.receiver = null; // indicates broadcasting
	}

	@Override
	public void fire() {
		if(receiver != null) { // there's a receiver => unicast the message
			this.node.send(msg, receiver);
		} else { // there's no reciever => broadcast the message
            log.logln("Broadcasteando");
			this.node.broadcast(msg);
		}
	}
}
