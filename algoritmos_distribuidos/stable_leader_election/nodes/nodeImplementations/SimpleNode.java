package projects.stable_leader_election.nodes.nodeImplementations;


import java.awt.Color;
import java.awt.Graphics;

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
				log.logln("INBOX: " + m.data);
			}
		}
	}

	@Override
	public void neighborhoodChange() {
	}
	
	@Override
	public void init() {
     log.logln("Fui inicializado ->>>> " + Double.toString(this.getRadioIntensity()));
	}

	@NodePopupMethod(menuText="Start")
	public void start() {
		log.logln("Start Routing from node " + this.ID + "\n");
		StartRound(0);
	}

	private void StartRound(int currentElectionRound) {
		int totalNodes = Tools.getNodeList().size();
        log.logln("Total de nós: " + Integer.toString(totalNodes));
		if(ID != (currentElectionRound % totalNodes + 1)) {
			SimpleMessage msg_teste = new SimpleMessage("Start," + Integer.toString(currentElectionRound));
	        this.sendDirect(msg_teste, Tools.getNodeByID( (currentElectionRound % totalNodes + 1) ));
		}
		currentRound = currentElectionRound;
		leader = (currentElectionRound % totalNodes) + 1;
		log.logln("Leader is: " + Integer.toString(leader));
	}

	@Override
	public void postStep() {
        StartRound(0);	
	}
	
	@Override
	public void preStep() {
	
	}


	@Override
	public void checkRequirements() throws WrongConfigurationException {
	
	}
}
