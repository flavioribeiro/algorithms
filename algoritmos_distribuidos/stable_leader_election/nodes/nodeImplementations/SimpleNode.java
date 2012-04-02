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

	/**
	 * the neighbor with the smallest ID
	 */
	public SimpleNode next;
	/**
	 * number of messages sent by this node in the current round
	 */
	public int msgSentInThisRound = 0;
	/**
	 * total number of messages sent by this node
	 */
	public int msgSent = 0;
	/**
	 * The amount to increment the data of the message each time it goes throug a node.
	 */
	public int increment = 0;

	Logging log = Logging.getLogger("stable_election_log");

	// a flag to prevent all nodes from sending messages
	public static boolean isSending = true;

	@Override
	public void handleMessages(Inbox inbox) {
		if(!isSending) { // don't even look at incoming messages
			return;
		}
        //Message msg = inbox.next();

        log.logln("rsrsrs\n");
		if(inbox.hasNext()) {
			Message msg = inbox.next();
			if(msg instanceof SimpleMessage) {
				SimpleMessage m = (SimpleMessage) msg;
				if(next != null) {
					m.data += increment;
					DelayTimer dt = new DelayTimer(m, this, m.data);
					dt.startRelative(m.data, this);
				}
			}
		}
	}

	@Override
	public void preStep() {
		msgSent += msgSentInThisRound;
		msgSentInThisRound = 0;
	}

	@Override
	public void init() {
		// initialize the node
//		try {
			// Read a value from the configuration file config.xml. 
			// The following command reads an integer, which is expected to
			// be stored in either of the two following styles in the XML file: 
			//    <S1Node>
			//       <increment value="2"/>
			//    </S1Node>
			// OR
			//    <S1Node increment="2"/>

//			increment = Configuration.getIntegerParameter("s1node/increment");
//		} catch(CorruptConfigurationEntryException e) {
			// Missing entry in the configuration file: Abort the simulation and
			// display a message to the user
//			Main.fatalError(e.getMessage());
//		}
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
	
	/* Methods with the annotation NodePopupMethod can be executed by the user from the
	 * GUI by clicking on the node and selecting the menu point in the popup menu.*/

	/**
	 * Initiate a message to be sent by this node in the next round. This starts the
	 * process of resending the message infinitely.
	 * 
	 * This method is part of the user-implemenation of this sample project. 
	 */
	@NodePopupMethod(menuText="Start")
	public void start() {
		// This sample project is designed for the round-based simulator. 
		// I.e. a node is only allowed to send a message when it is its turn.
		// To comply with this rule, we're not allowed to call the 
		// method 'SendMessage()' here, but need either to remember that the
		// user has clicked to send a message and then send it in the intervalStep()
		// manually. Here, we show a simpler and more elegant approach: 
		// Set a timer (with time 1), which will fire the next time this node is
		// handled. The defaultProject already contains a MessageTimer which can 
		// be used for exactly this purpose.
		MessageTimer msgTimer = new MessageTimer(new SimpleMessage(1)); // broadcast
		msgTimer.startRelative(1, this);
		Tools.appendToOutput("Start Routing from node " + this.ID + "\n");
	}
	
	/* (non-Javadoc)
	 * @see sinalgo.nodes.Node#draw(java.awt.Graphics, sinalgo.gui.transformation.PositionTransformation, boolean)
	 */
	public void draw(Graphics g, PositionTransformation pt, boolean highlight) {
		// set the color of this node
		this.setColor(new Color((float) 0.5/(1+msgSentInThisRound), (float) 0.5, (float) 1.0/(1+msgSentInThisRound)));
		String text = Integer.toString(msgSent) + "|" + msgSentInThisRound;
		// draw the node as a circle with the text inside
		super.drawNodeAsDiskWithText(g, pt, highlight, text, 10, Color.YELLOW);
		//super.drawNodeAsSquareWithText(g, pt, highlight, text, 10, Color.YELLOW);
	}

	@Override
	public void postStep() {
		
	}

	@Override
	public String toString() {
		return "Messages sent so far: " + msgSent + "\nMessages sent in this round: " + msgSentInThisRound;
	}

	@Override
	public void checkRequirements() throws WrongConfigurationException {
		if(increment < 0) {
			throw new WrongConfigurationException("SimpleNode: The increment value (specified in the config file) must be greater or equal to 1.");
		}
	}
}
