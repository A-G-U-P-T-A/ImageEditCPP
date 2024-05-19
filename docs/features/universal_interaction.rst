Universal Interaction System
============================

The Universal Interaction System provides a mechanism to enable interactions between different game entities. It's primarily designed for developers using the Unreal Engine Blueprints system.

How to Integrate the Universal Interaction System
--------------------------------------------------

**Adding the Universal Interaction Component to a Character**

1. Open the character's Blueprint in the Unreal Engine Editor.
2. In the Components panel, click on "Add Component", then search for and select ``UniversalInteractionComponent``.
3. With the Universal Interaction Component selected, locate the Details panel to configure the component properties. 

**Initializing the Universal Interaction Component**

Once the Universal Interaction Component has been added to a character, it needs to be initialized:

1. Go to the character's Blueprint Event Graph.
2. Find or create the appropriate event where you want to initialize the interaction system (for example, `BeginPlay`).
3. Drag the Universal Interaction Component into the event graph to get a reference to it.
4. From the Universal Interaction Component reference, drag out a node and search for the `Init` function. Connect this to your event.
5. For the `Init` function's `NewCamera` parameter, provide a reference to the camera component you wish to use for the interactions.

**Interacting with Actors**

To enable interaction with specific actors:

1. Open the target actor's Blueprint in the Unreal Engine Editor.
2. Make sure that the actor implements the `UniversalInteractionInterface` (you can check this in the Class Settings).
3. In the actor's Blueprint, go to the Event Graph.
4. Right click on the graph and search for the events `InteractionAssistStart`, `InteractionAssistStop`, and `BeginInteraction`. These are the events that will fire when the actor is to start assisting interaction, stop assisting, and begin an interaction respectively. You can now provide custom script for what you want to happen at these events.

Please note that the actors with which the character will interact need to have the appropriate collision components and settings to ensure they are detectable by the Universal Interaction Component's line trace. Adjust these properties in the Blueprint's Details panel as needed.

**Creating an Inspect Actor**

An `InspectActor` is a special type of actor that can be inspected. To create one:

1. In the Content Browser, click on the "Add New" button, select "Blueprint Class", and then choose `InspectActor` as the parent class.
2. Open the new Blueprint, and in the Event Graph, search for and implement the `BeginInteraction` event to define what should happen when this actor is inspected.

By using these methods, you can effectively control and customize how different entities in your game world interact with each other.
