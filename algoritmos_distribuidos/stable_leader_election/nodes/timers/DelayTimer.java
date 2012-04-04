package projects.stable_leader_election.nodes.timers;

import projects.stable_leader_election.nodes.nodeImplementations.SimpleNode;
import sinalgo.nodes.messages.Message;
import sinalgo.nodes.timers.Timer;
import sinalgo.tools.logging.Logging;

public class DelayTimer extends Timer {
	Message msg;
	SimpleNode sender;
	Logging log = Logging.getLogger("stable_election_log");
	int interval;

	public DelayTimer(Message msg, SimpleNode sender, int interval) {
        log.logln("chegou aqui");
		this.msg = msg;
		this.sender = sender;
		this.interval = interval;
	}

	@Override
	public void fire() {
		if(!SimpleNode.isSending) {
			return;
		}
		if(sender.next != null) {
			node.send(msg, sender.next);
            log.logln("enviei a msg!111");
//			((SimpleNode) node).msgSentInThisRound++;
		}
		this.startRelative(interval, node); // recursive restart of the timer
    }
}


