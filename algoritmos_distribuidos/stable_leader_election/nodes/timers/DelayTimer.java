/*
 Copyright (c) 2007, Distributed Computing Group (DCG)
                    ETH Zurich
                    Switzerland
                    dcg.ethz.ch

 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:

 - Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

 - Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

 - Neither the name 'Sinalgo' nor the names of its contributors may be
   used to endorse or promote products derived from this software
   without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
package projects.stable_leader_election.nodes.timers;

import projects.stable_leader_election.nodes.nodeImplementations.SimpleNode;
import sinalgo.nodes.messages.Message;
import sinalgo.nodes.timers.Timer;
import sinalgo.tools.logging.Logging;

/**
 * A timer that sends a message repeatedly with some delay. The method
 * stops sending the message when the connection to the receiver is broken up. 
 * <p> 
 * Note that the timer object knows the node which has started this
 * timer. However, this information is only set while the timer is started
 * and therefore may only be accessed in the <code>fire</code> method. 
 */
public class DelayTimer extends Timer {
	Message msg;
	SimpleNode sender;
	Logging log = Logging.getLogger("stable_election_log");
	int interval;
	
	/**
	 * Creates a new Timer object which will send the message repeatedly 
	 * to the receiver. The delay between the successive firings of the timer
	 * is indicated by interval. The timer needs to be started initially, with
	 * an arbitrary delay, after which the first message is sent. All subsequent
	 * messages are sent with the given interval. 
	 *
	 * @param msg Message to be sent. 
	 * @param sender The sender of the message.
	 * @param interval Interval between subsequent firings of the timer.
	 */
	public DelayTimer(Message msg, SimpleNode sender, int interval) {
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
			((SimpleNode) node).msgSentInThisRound++;
		}
		this.startRelative(interval, node); // recursive restart of the timer
	}
}
