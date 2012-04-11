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

public class SimpleNode extends Node {

    public int currentStep = 0; //rounds at sinalgo will behave as steps here
    public int stepsWithoutOK = 0;
	private int currentRound;
	private int leader;
    private int interval = 2;

	Logging log = Logging.getLogger("stable_election_log");

	@Override
	public void handleMessages(Inbox inbox) {
		if(inbox.hasNext()) {
			Message msg = inbox.next();

            SimpleMessage m = (SimpleMessage) msg;
            log.logln("[" + ID + "] INBOX: " + m.data);
            if (m.data.startsWith("START") && m.data.endsWith(Integer.toString(ID))) {
                log.logln("[" + ID + "] Hey, it seems i'm the leader now. Broadcasting OK");
                SimpleMessage ok_msg = new SimpleMessage("OK," + Integer.toString(ID));
                this.broadcast(ok_msg);
                stepsWithoutOK = 0;

            } else if (m.data.startsWith("OK") && m.data.endsWith(Integer.toString(getLeader()))) {
                log.logln("[" + ID + "] Received OK from the leader");
                stepsWithoutOK = 0;
            }

		}
	}

    @Override
	public void init() {
        setLeader(0);
        setCurrentRound(0);
        log.logln("[" + ID + "] Initialized (Current Round: " + Integer.toString(currentRound) + " / Current Leader: " + Integer.toString(leader));
	}

	@NodePopupMethod(menuText="Start")
	public void start() {
	}

	@Override
	public void postStep() {
        log.logln("[" + ID + "] Current Round: " + Integer.toString(currentRound) + " / Current Leader: " + Integer.toString(leader));
	}

	@Override
	public void preStep() {
        currentStep++;
        stepsWithoutOK++;

        if (stepsWithoutOK > (2 * interval + 1)) {
            log.logln("[" + ID + "] Timeout expired without OK. It seems we haven't leader.");
            int newLeader = currentRound % Tools.getNodeList().size() + 1;
            setLeader(newLeader);
            setCurrentRound(getCurrentRound() + 1);

            SimpleMessage msg = new SimpleMessage("START," + Integer.toString(newLeader));
            this.sendDirect(msg, Tools.getNodeByID(newLeader));
            stepsWithoutOK = 0;
        }
	}

	@Override
	public void neighborhoodChange() {
	}

	@Override
	public void checkRequirements() throws WrongConfigurationException {
	}

    private void setLeader(int newLeader) {
        log.logln("[" + ID + "] Setting a new leader: " + Integer.toString(newLeader));
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
}
