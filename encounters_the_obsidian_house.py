figment = {
	"Start" : {
		"Prompt" : """\nAs you take the book from the desk,\
		\nan electric shock runs down your back.\
		\nForming from the dense air in the shack,\
		\na figure of dark purple and black energy leans forward.\
		\nTheir eyes aglow with deep crimson, they measure you.\
		\nA clawed hand extends and the figment waits.
		""",
		"Choice" : {
			"1" : ["Run", "Flee"],
			"2" : ["Give book", "Give book calm"],
			"3" : ["Attack!", "Combat"],
			"4" : ["Attempt to communicate", "Diplomacy"]
		}
	},
	"Give book calm" : {
		"Prompt" : """\nThe figment nods to you in appreciation.\
		\nIt dissipates, leaving no trace of itself or the book.
		""",
		"Return" : {
			"Player Remove" : "old book",
			"Event" : ["figment", False]
		},
		"Exit" : "End"
	},
	"Flee" : {
		"Check" : [["dexterity", 7], ["focus", 7]],
		"Passed" : {
			"Prompt" : """\nFleeing the structure, you notice a rise in temperature.\
			\nOver your shoulder, you see a shadow fall over the shack.\
			\nEyes watch you from within.
			""",
			"Return" : {
				"Event1" : ["figment", False],
				"Event2" : ["shack cursed", True],
				"Relocate" : "front tavern",
				"return" : "Fled"
			},
			"Exit" : "End"
		},
		"Failed" : {
			"Prompt" : "\nA claw, electric and sharp, slashes your back causing you to fall.\n",
			"Status" : {"Player health" : -15},
			"Choice" : {
				"1" : ["Give up the book and crawl away", "Crawl no book"],
				"2" : ["Hold on to the book and crawl away", "Crawl book"],
				"3" : ["Attempt to attack while prone", "Crawl book"]
			}
		}
	},
	"Crawl no book" : {
		"Prompt" : "\nThere is a screeching cry. When your eyes open, the figment and book are gone.\n",
		"Status" : {"Player mental" : -5},
		"Return" : {
			"Player remove" : "old book",
			"Event" : ["figment", False]
		},
		"Exit" : "End"
	},
	"Crawl book" : {
		"Prompt" : """\nThe figment lifts a claw and crushes your leg.\
		\nStill in the throws of pain, you notice the figment and book are gone.
		""",
		"Status" : {"Player health" : -25, "leg_crippled" : True},
		"Return" : {
			"Player remove" : "old book",
			"Event" : ["figment", False]
		},
		"Exit" : "End"
	},
	"Combat" : {
		"Prompt" : "\nHow to proceed?\n",
		"Check" : [["inventory", "dagger"],["inventory", "chunk of metal"]],
		"Passed" : {
			"Choice" : {
				"1" : ["Unarmed attack", "Punch"],
				"2" : ["Dagger attack", "Dagger"],
				"3" : ["Concentrate on chunk of metal", "Metal"]
			}
		},
		"Failed" : {
			"Check dagger" : ["inventory", "dagger"],
			"Choice dagger" : {
				"1" : ["Unarmed attack", "Punch"],
				"2" : ["Dagger attack", "Dagger"]
			},
			"Check metal" : ["inventory", "chunk of metal"],
			"Choice metal" : {
				"1" : ["Unarmed attack", "Punch"],
				"2" : ["Concentrate on chunk of metal", "Metal"]
			},
			"Choice" : {
				"1" : ["Unarmed attack", "Punch"]
			}
		}
	},
	"Punch" : {
		"Prompt" : """\nYour fist makes contact with the body of the figment.\
		\ngoing numb and limp. As you recoil, a sharp pain erupts in your skull.
		""",
		"Status" : {"Player health" : -10, "Player mental" : -10},
		"Choice" : {
			"1" : ["Run", "Flee"],
			"2" : ["Punch again", "Last punch"],
			"3" : ["Give book", "Give book angry"]
		}
	},
	"Dagger" : {
		"Prompt" : "Gripping the dagger with familiarity, you lunge for the figment.",
		"Check" : [["dexterity", 8],["focus", 4]],
		"Passed" : {
			"Jump" : "Combat Success"
		},
		"Failed" : {
			"Prompt" : """\nYour dagger makes contact with the figment.\
			\nThe blade vibrates in your grasp, begins to glow a bright red,\
			\nthen vanishes in a burst of sparks. Your brain ignites with pain.
			""",
			"Status" : {"Player mental" : -10},
			"Return" : ["Player remove", "dagger"],
			"Choice" : {
				"1" : ["Run", "Flee"],
				"2" : ["Unarmed attack, Last punch"],
				"3" : ["Give book", "Give book angry"]
			}
		}
	},
	"Metal" : {
		"Prompt" : """\nA subdued memory is pulled from your mind.\
		\nThe chunk of metal seems to absorb your thoughts before\
		\na burst of energy erupts around the figment.
		""",
		"Check" : ["focus", 5],
		"Passed" : {
			"Jump" : "Combat success"
		},
		"Failed" : {
			"Prompt" : """\nThe energy dissolves as quickly as it appeared.\
			\nThe figment seems unharmed. Your head aches.
			""",
			"Status" : {"Player mental" : -10},
			"Choice" : {
				"1" : ["Run", "Flee"],
				"2" : ["Unarmed attack", "Last punch"],
				"3" : ["Give book", "Give book angry"]
			}
		}
	},
	"Last punch" : {
		"Prompt" : """\nYou step forward to punch when another bolt\
		\nof pain courses through your head.\
		\nWhen it subsides and you open your eyes, the book and figment\
		\nare gone.
		""",
		"Status" : {"Player mental" : -10},
		"Return" : {
			"Player remove" : "old book",
			"Event" : ["figment", False]
		},
		"Exit" : "End"
	},
	"Give book angry" : {
		"Prompt" : """\nThe book is snatched from your hand.\
		\nAs the figment fades, its eyes linger a moment longer,\
		\nburning their glow into your mind.
		""",
		"Return" : {
			"Player remove" : "old book",
			"Event" : ["figment", False]
		},
		"Exit" : "End"
	},
	"Combat success" : {
		"Prompt" : """\nThe figment releases a scream that shivers your nerve endings.\
		\nAs the sound dims, you sense sorrow within it.\
		\nThere is a flicker as the figment fades and the shack becomes still.
		""",
		"Status" : {"Player mental" : -10},
		"Return" : {
			"Event" : ["figment", False]
		},
		"Exit" : "End"
	},
	"Diplomacy" : {
		"Prompt" : """\nYou stop and face the figment.\
		\nAs you attempt to form words, it stares...considering.
		""",
		"Check" : [["charisma", 5], ["focus", 7]],
		"Passed" : {
			"Prompt" : """Before words have left your lips,\
			\na claw rests on your shoulder. The figment gazes into\
			\nyour eyes and a voice ripples through your thoughts.\
			\n\n"This world is not guaranteed. Knowledge can be erased,\
			\nlife can be ended...and all that you have fought for will\
			\nbe for nothing."\
			\n\nThe figment slowly nods as its grip on your shoulder is\
			\nreleased. The room becomes warm and the dark shape dissipates.
			""",
			"Return" : {
				"Event" : ["figment", False],
			},
			"Exit" : "End"
		},
		"Failed" : {
			"Prompt" : """The figment leans closer as your mouth\
			\nfails to form any sound.\
			\n\n"Fools supply themselves to the fallen Dark.\
			\nThe Deceiver spins thread and the Sculptor hungers.\
			\nYou will not stand against them, but their arrival will\
			\ndistract nonetheless.\
			\nBlind your ignorance. The Seer has studied long and the\
			\nhour grows late."
			\n\nThe figment gently curls its claws around the book in\
			\nyour hand. It gives you one last glance before dissipating.\
			\nThe book is gone.
			""",
			"Return" : {
				"Player remove" : "old book",
				"Event" : ["figment", False]
			},
			"Exit" : "End"
		}
	},
	"End" : {
		"the love you take" : "the love you make"
	}
}