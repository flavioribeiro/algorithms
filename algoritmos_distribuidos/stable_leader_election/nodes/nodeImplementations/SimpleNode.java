package projects.stable_leader_election.nodes.nodeImplementations;

import java.awt.Color;
import java.awt.Graphics;

import projects.defaultProject.nodes.timers.MessageTimer;
import projects.stable_leader_election.nodes.messages.SimpleMessage;
import projects.stable_leader_election.nodes.timers.DelayTimer;
import sinalgo.configuration.WrongConfigurationException;
import sinalgo.nodes.Node;
import sinalgo.nodes.messages.Inbox;
import sinalgo.nodes.messages.Message;
import sinalgo.runtime.Main;
import sinalgo.tools.Tools;
import sinalgo.tools.logging.Logging;

import sinalgo.gui.transformation.PositionTransformation;

public class SimpleNode extends Node {

    public int currentStep = 0; //rounds at sinalgo will behave as steps here
    public int stepsWithoutOK = 0;
	private int currentRound;
	private int leader;
    private int interval = 4;
    private Boolean isCrashed = false;

	Logging log = Logging.getLogger("stable_election_log");

	@Override
	public void handleMessages(Inbox inbox) {
        if (isCrashed) {
            privlog("I'm crashed!");
            return;
        }
		if(inbox.hasNext()) {
			Message msg = inbox.next();

            SimpleMessage m = (SimpleMessage) msg;
            if (m.data.startsWith("START") && m.data.endsWith(Integer.toString(ID))) {
                privlog("Hey, it seems i'm the leader now. Broadcasting OK");
                setLeader(ID);
                broadcastOK();

           } else if (m.data.startsWith("OK") && m.data.endsWith(Integer.toString(getLeader()))) {
                privlog("Received OK from the leader");
                stepsWithoutOK = 0;
           }
           inbox.freePackets();
		}
	}

	@Override
	public void draw(Graphics g, PositionTransformation pt, boolean highlight) {
        super.drawNodeAsDiskWithText(g, pt, highlight, Integer.toString(this.ID), 26, Color.WHITE);
	}

    @Override
	public void init() {
        setLeader(1);
        setCurrentRound(1);
        privlog("Initialized (Current Round: " + Integer.toString(currentRound) + " / Current Leader: " + Integer.toString(leader));
	}

	@NodePopupMethod(menuText="Start")
	public void start() {
	}

    @NodePopupMethod(menuText="Crash")
    public void crash() {
        isCrashed = true;
        this.setColor(Color.RED);
    }

    @NodePopupMethod(menuText="Recover")
    public void recover() {
        isCrashed = false;
        this.setColor(Color.BLACK);

        if (inbox.hasNext()) {
            Message msg = inbox.next();
            SimpleMessage m = (SimpleMessage) msg;

            if (m.data.startsWith("STOP")) {
                privlog("Received STOP");
                int newLeader = currentRound % Tools.getNodeList().size() + 1;
                setLeader(newLeader);
                setCurrentRound(getCurrentRound() + 1);
                inbox.freePackets();
            }
        }
    }

	@Override
	public void postStep() {
        privlog("Current Round: " + Integer.toString(currentRound) + " / Current Leader: " + Integer.toString(leader));
	}

	@Override
	public void preStep() {
        if (isCrashed) {

            return;
        } else {
            currentStep++;
            stepsWithoutOK++;

            if (stepsWithoutOK > (2 * interval + 1)) {
                privlog("Timeout expired without OK. It seems we haven't leader. Sending STOP to the old leader");

                SimpleMessage msg = new SimpleMessage("STOP," + Integer.toString(getLeader()));
                this.sendDirect(msg, Tools.getNodeByID(getLeader()));

                int newLeader = currentRound % Tools.getNodeList().size() + 1;
                setLeader(newLeader);
                setCurrentRound(getCurrentRound() + 1);
                sendStartMessageToLeader();
            } else if ((stepsWithoutOK % interval == 0) && (getLeader() == ID)) {
                privlog("OK, i'm the leader and still alive");
                broadcastOK();
            }
        }
	}

	@Override
	public void neighborhoodChange() {
	}

	@Override
	public void checkRequirements() throws WrongConfigurationException {
	}

    public void privlog(String message) {
        log.logln("[Nó " + ID + "] " + message);
    }

    private void setLeader(int newLeader) {
        privlog("Setting a new leader: " + Integer.toString(newLeader));
        if (newLeader == ID) {
            this.setColor(Color.GREEN);
        } else {
            this.setColor(Color.BLACK);
        }

        this.leader = newLeader;
    }

    private int getLeader() {
        return this.leader;
    }

    private void setCurrentRound(int newRound) {
        this.currentRound = newRound;
    }

    private int getCurrentRound() {
        return currentRound;
    }

    private void broadcastOK() {
        SimpleMessage ok_msg = new SimpleMessage("OK," + Integer.toString(ID));
        this.broadcast(ok_msg);
        stepsWithoutOK = 0;
    }

    private void sendStartMessageToLeader() {
        SimpleMessage msg = new SimpleMessage("START," + Integer.toString(getLeader()));
        this.sendDirect(msg, Tools.getNodeByID(getLeader()));
        stepsWithoutOK = 0;
    }
}
