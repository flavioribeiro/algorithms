package projects.stable_leader_election.nodes.nodeImplementations;


import java.awt.Color;
import java.awt.Graphics;

import projects.stable_leader_election.nodes.timers.MyMessageTimer;
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

public class SimpleNode extends Node {

    public SimpleNode next;
	int currentRound = 0;
	int leader = 0;

	Logging log = Logging.getLogger("stable_election_log");

	// a flag to prevent all nodes from sending messages
	public static boolean isSending = true;

	@Override
	public void handleMessages(Inbox inbox) {
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
	public void neighborhoodChange() {
		next = null;
		for(Edge e : this.outgoingConnections) {
			if(next == null) {
				next = (SimpleNode) e.endNode;
			} else {
				if(e.endNode.ID < next.ID) {
					next = (SimpleNode) e.endNode;
				}
			}
		}
	}
	
	@Override
	public void init() {
		StartRound(0);
//        MessageTimer msgTimer = new MessageTimer(new SimpleMessage("Rolou!"), Tools.getNodeByID(1));
   			MyMessageTimer msgTimer = new MyMessageTimer(new SimpleMessage("StartRound"));//SimpleMessage("Start," + Integer.toString(currentElectionRound)),
                                                           //                 Tools.getNodeByID(0));
			msgTimer.startRelative(1, this);

     log.logln("Fui inicializado");
	}

	@NodePopupMethod(menuText="Start")
	public void start() {
		MyMessageTimer msgTimer = new MyMessageTimer(new SimpleMessage("risos"));
		msgTimer.startRelative(1, this);
		log.logln("Start Routing from node " + this.ID + "\n");
	}
	

	private void StartRound(int currentElectionRound) {
		int totalNodes = Tools.getNodeList().size();
        log.logln("Total de nós: " + Integer.toString(totalNodes));
//		if(ID != currentElectionRound % totalNodes) {
			MyMessageTimer msgTimer = new MyMessageTimer(new SimpleMessage("StartRound"));//SimpleMessage("Start," + Integer.toString(currentElectionRound)),
                                                           //                 Tools.getNodeByID(0));
			msgTimer.startRelative(1, this);
//		}
//		currentRound = currentElectionRound;
//		leader = currentElectionRound % totalNodes;
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
