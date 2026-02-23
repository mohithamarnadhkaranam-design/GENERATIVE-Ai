{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyOuvRAx3m157ZHT4qWmsijL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mohithamarnadhkaranam-design/GENERATIVE-Ai/blob/main/Sentiment_Analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LQoVN1pxFIrL"
      },
      "outputs": [],
      "source": [
        "# Install if needed\n",
        "# !pip install transformers torch pandas\n",
        "\n",
        "from transformers import pipeline\n",
        "import pandas as pd\n",
        "\n",
        "# Load sentiment analysis model\n",
        "sentiment = pipeline(\"sentiment-analysis\")\n",
        "\n",
        "# Sample product review (you can change this text)\n",
        "reviews = \"\"\"\n",
        "The laptop starts quickly and works smoothly for daily tasks.\n",
        "The screen quality is clear and good for watching videos.\n",
        "Battery backup is average and needs charging often.\n",
        "The fan makes noise when many apps are running.\n",
        "Overall, it is a good laptop for students but not for gaming.\n",
        "\"\"\"\n",
        "\n",
        "# Split review into sentences\n",
        "sentences = reviews.split(\". \")\n",
        "\n",
        "pros = []\n",
        "cons = []\n",
        "\n",
        "for s in sentences:\n",
        "    s = s.strip()\n",
        "    if s == \"\":\n",
        "        continue\n",
        "\n",
        "    result = sentiment(s)[0]\n",
        "\n",
        "    if result[\"label\"] == \"POSITIVE\":\n",
        "        pros.append(s)\n",
        "    elif result[\"label\"] == \"NEGATIVE\":\n",
        "        cons.append(s)\n",
        "\n",
        "# Take only 2 pros and 2 cons\n",
        "pros = pros[:2]\n",
        "cons = cons[:2]\n",
        "\n",
        "# 🔧 Make both lists same length by padding with \"\"\n",
        "max_len = max(len(pros), len(cons))\n",
        "\n",
        "while len(pros) < max_len:\n",
        "    pros.append(\"\")\n",
        "\n",
        "while len(cons) < max_len:\n",
        "    cons.append(\"\")\n",
        "\n",
        "# Create table\n",
        "df = pd.DataFrame({\n",
        "    \"Pros\": pros,\n",
        "    \"Cons\": cons\n",
        "})\n",
        "\n",
        "df"
      ]
    }
  ]
}