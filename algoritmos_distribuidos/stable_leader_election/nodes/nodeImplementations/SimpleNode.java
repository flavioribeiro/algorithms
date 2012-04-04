package projects.stable_leader_election.nodes.nodeImplementations;


import java.awt.Color;
import java.awt.Graphics;

import projects.defaultProject.nodes.timers.MessageTimer;
import projects.stable_leader_election.nodes.messages.SimpleMessage;
import projects.stable_leader_election.nodes.timers.DelayTimer;
import sinalgo.configuration.Configuration;
import sinalgo.configuration.CorruptConfigurationEntryException;
import sinalgo.configuration.WrongConfigurationException;
import sinalgo.gui.transformation.PositionTransformation;
import sinalgo.nodes.Node;
import sinalgo.nodes.edges.Edge;
import sinalgo.nodes.messages.Inbox;
import sinalgo.nodes.messages.Message;
import sinalgo.runtime.Main;
import sinalgo.tools.Tools;
import sinalgo.tools.logging.Logging;

/**
 * The Node of the sample project.
 */
public class SimpleNode extends Node {

	int currentRound = 0;
	int leader = 0;

	Logging log = Logging.getLogger("stable_election_log");

	// a flag to prevent all nodes from sending messages
	public static boolean isSending = true;

	@Override
	public void handleMessages(Inbox inbox) {
		log.logln(Integer.toString(inbox.size()));
		if(inbox.hasNext()) {
			log.logln("teste2");
			Message msg = inbox.next();
			if(msg instanceof SimpleMessage) {
				SimpleMessage m = (SimpleMessage) msg;
				log.logln(m.data);
			}
		}
	}

	@Override
	public void init() {
		StartRound(0);
	}


	private void StartRound(int currentElectionRound) {
		int totalNodes = Tools.getNodeList().size();
		if(ID != currentElectionRound % totalNodes) {
			MessageTimer msgTimer = new MessageTimer(new SimpleMessage("Start," + Integer.toString(currentElectionRound)), Tools.getNodeByID(currentElectionRound % totalNodes));
			msgTimer.startRelative(1, this);
		}
		currentRound = currentElectionRound;
		leader = currentElectionRound % totalNodes;
	}

	@Override
	public void neighborhoodChange() {
	
	}
	
	@Override
	public void postStep() {
	
	}
	
	@Override
	public void preStep() {
	
	}


	@Override
	public void checkRequirements() throws WrongConfigurationException {
	
	}
}
